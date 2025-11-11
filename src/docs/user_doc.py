def doc_ottieni_utenti():
    return {
        "responses": {
            "200": {
                "description": "Lista di utenti",
                "examples": {
                    "application/json": [
                            {"id": 1, "username": "Alice" , "email": "alice@example.com"},
                            {"id": 2, "username": "Bob", "email": "bob@example.com"}
                ]
                }
            }
        }
    }