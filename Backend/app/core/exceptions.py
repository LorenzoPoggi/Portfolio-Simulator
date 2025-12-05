# excepciones.py
from fastapi import HTTPException, status

# Diccionario con excepciones mas usadas en la practica
excepciones = {
    "no_autorizado": HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"Error": "Credenciales inválidas"},
        headers={"WWW-Authenticate": "Bearer"}
    ),
    "usuario_no_encontrado": HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"Error": "Usuario no encontrado"}
    ),
    "usuario_deshabilitado": HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={"Error": "Usuario deshabilitado"}
    ),
    "no_tiene_permisos": HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={"Error": "No tiene permisos para esta acción"}
    ),
    "usuario_ya_registrado": HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "El username ya está registrado"}
    ),
    "email_ya_registrado": HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "El email ya está registrado"}
    ),
    "contrasena_incorrecta": HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"Error": "Contraseña incorrecta"}
    ),
    "usuario_inactivo": HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, 
        detail= {'Error:': 'Usuario inactivo'})
}