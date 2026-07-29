from ai_engine.api_gateway import ASEOGateway



gateway = ASEOGateway()



result = gateway.gateway_request(

    "Startup Company",

    50

)



print(result)