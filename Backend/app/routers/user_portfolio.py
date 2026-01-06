# user_portfolio.py

from fastapi import APIRouter, Depends, HTTPException, status
from database.models.models import *
from core.security import *
from services.api_external import busqueda_symbol
from schemas.stock import Stock_Purchase_Request, Stock_Purchase_Response

# Inicializacion del Router
router = APIRouter(tags=['Portfolio'])

# Operacion para visualizar mi Portfolio
@router.get('/miportfolio', response_model= list[Stock_Purchase_Response], status_code= status.HTTP_200_OK)
async def view_my_portfolio(user: User = Depends (current_user), db: Session = Depends (get_db)):
    portfolio = db.query(User_Portfolio).filter(User_Portfolio.user_id == user.id).all()
    result: list[Stock_Purchase_Response] = []
    for feature in portfolio:
        currency = feature.stock.currency if getattr(feature, 'stock', None) and feature.stock is not None else 'USD'
        result.append(Stock_Purchase_Response(
            symbol=feature.symbol,
            quantity=feature.quantity,
            price=feature.buy_price,
            total_spent=feature.total_invested,
            currency=currency
        ))
    return result

# Operacion para "comprar" una accion y guardarla en el Portfolio
@router.post('/mercado/stock/{symbol}', response_model= Stock_Purchase_Response, status_code= status.HTTP_201_CREATED)
async def buy_stock (symbol: str, purchase: Stock_Purchase_Request, db: Session = Depends(get_db), user: User = Depends(current_user)):
    if purchase.quantity <= 0 or purchase.quantity > 5:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                            detail= 'Indique una cantidad entre 1 y 5 para su compra.')
    data = await busqueda_symbol(symbol)
    if not data or "data" not in data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail="Accion no encontrada.")
    symbol_data = data["data"]
    price = symbol_data.get('price')
    if price is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Precio no disponible para la acción.")
    currency = symbol_data.get('currency', 'USD')
    total_spent = price * purchase.quantity
    portfolio_entry = User_Portfolio(
        user_id = user.id,
        symbol = symbol,
        quantity = purchase.quantity,
        buy_price = price,
        total_invested = total_spent
    )
    db.add(portfolio_entry)
    db.commit()
    db.refresh(portfolio_entry)
    return Stock_Purchase_Response(
        symbol = symbol,
        quantity = purchase.quantity,
        price = price,
        total_spent = total_spent,
        currency = currency
    )

# Operacion para "vender" una accion de mi Portfolio
@router.delete('/miportfolio/{symbol}', status_code= status.HTTP_204_NO_CONTENT)
async def delete_stock(symbol: str, user: User = Depends(current_user), db: Session = Depends(get_db)):
    stock = db.query(User_Portfolio).filter(User_Portfolio.symbol == symbol, User_Portfolio.user_id == user.id).first()
    if not stock:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= 'Accion no encontrada en el Portfolio.')
    db.delete(stock)
    db.commit()
    return 'Accion vendida con éxito, puede seguir comprando.'