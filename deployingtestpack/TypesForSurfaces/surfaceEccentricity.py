from RFEM.initModel import Model, clearAtributes

class SurfaceEccentricity():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Surface Eccentricity
        clientObject = model.clientModel.factory.create('ns0:surface_eccentricity')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Surface Eccentricity No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Surface Eccentricity to client model
        model.clientModel.service.set_surface_eccentricity(clientObject)