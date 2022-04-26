from RFEM.initModel import Model, clearAtributes

class EnlargedColumnHead():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Enlarged Column Head
        clientObject = model.clientModel.factory.create('ns0:enlarged_column_head')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Enlarged Column Head No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Enlarged Column Head to client model
        model.clientModel.service.set_enlarged_column_head(clientObject)