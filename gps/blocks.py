from gps import gps

problem = {
    "init": ["Espaço vazio em A", "bloco A no espaço B", "bloco B no espaço C", " C sobre a bancada", "espaço na bancada"],
    "finish": ["Espaço vazio em C", "bloco C no espaço B", "B sobre A", "A sobre a bancada", "espaço na bancada"],
    
    "ops": [
        {
            "action": "Move A de B para C",
            "preconds": [
                "Espaço vazio em A",
                "Espaço vazio em C",
                "bloco A no espaço B"
            ],
            "add": [
                "A sobre C",
                "Espaço vazio em B"
            ],
            "delete": [
                "bloco A no espaço B",
                "Espaço vazio em C"
            ]
        },
        {
            "action": "Mova A da bancada para B",
            "preconds": [
                "Espaço vazio em A",
                "Espaço vazio em B",
                "A sobre a bancada"
            ],
            "add": [
                "bloco A no espaço B"
            ],
            "delete": [
                "A sobre a bancada",
                "Espaço vazio em B"
            ]
        },
        {
            "action": "move A de B para a bancada",
            "preconds": [
                "Espaço vazio em A",
                "espaço na bancada",
                "bloco A no espaço B"
            ],
            "add": [
                "A sobre a bancada",
                "Espaço vazio em B"
            ],
            "delete": [
                "bloco A no espaço B"
            ]
        },
        {
            "action": "move A de C para B",
            "preconds": [
                "Espaço vazio em A",
                "Espaço vazio em B",
                "A sobre C"
            ],
            "add": [
                "bloco A no espaço B",
                "Espaço vazio em C"
            ],
            "delete": [
                "A sobre C",
                "Espaço vazio em B"
            ]
        },
        {
            "action": "move a from table to c",
            "preconds": [
                "Espaço vazio em A",
                "Espaço vazio em C",
                "A sobre a bancada"
            ],
            "add": [
                "A sobre C"
            ],
            "delete": [
                "A sobre a bancada",
                "Espaço vazio em C"
            ]
        },
        {
            "action": "move a from c to table",
            "preconds": [
                "Espaço vazio em A",
                "espaço na bancada",
                "A sobre C"
            ],
            "add": [
                "A sobre a bancada",
                "Espaço vazio em C"
            ],
            "delete": [
                "A sobre C"
            ]
        },
        {
            "action": "move b from a to c",
            "preconds": [
                "Espaço vazio em B",
                "Espaço vazio em C",
                "B sobre A"
            ],
            "add": [
                "bloco B no espaço C",
                "Espaço vazio em A"
            ],
            "delete": [
                "B sobre A",
                "Espaço vazio em C"
            ]
        },
        {
            "action": "move b from table to a",
            "preconds": [
                "Espaço vazio em B",
                "Espaço vazio em A",
                "B sobre a  bancada"
            ],
            "add": [
                "B sobre A"
            ],
            "delete": [
                "B sobre a  bancada",
                "Espaço vazio em A"
            ]
        },
        {
            "action": "move b from a to table",
            "preconds": [
                "Espaço vazio em B",
                "espaço na bancada",
                "B sobre A"
            ],
            "add": [
                "B sobre a  bancada",
                "Espaço vazio em A"
            ],
            "delete": [
                "B sobre A"
            ]
        },
        {
            "action": "Move B de C para A",
            "preconds": [
                "Espaço vazio em B",
                "Espaço vazio em A",
                "bloco B no espaço C"
            ],
            "add": [
                "B sobre A",
                "Espaço vazio em C"
            ],
            "delete": [
                "bloco B no espaço C",
                "Espaço vazio em A"
            ]
        },
        {
            "action": "move b from table to c",
            "preconds": [
                "Espaço vazio em B",
                "Espaço vazio em C",
                "B sobre a  bancada"
            ],
            "add": [
                "bloco B no espaço C"
            ],
            "delete": [
                "B sobre a  bancada",
                "Espaço vazio em C"
            ]
        },
        {
            "action": "move b from c to table",
            "preconds": [
                "Espaço vazio em B",
                "espaço na bancada",
                "bloco B no espaço C"
            ],
            "add": [
                "B sobre a  bancada",
                "Espaço vazio em C"
            ],
            "delete": [
                "bloco B no espaço C"
            ]
        },
        {
            "action": "move c from a to b",
            "preconds": [
                "Espaço vazio em C",
                "Espaço vazio em B",
                "c on a"
            ],
            "add": [
                "bloco C no espaço B",
                "Espaço vazio em A"
            ],
            "delete": [
                "c on a",
                "Espaço vazio em B"
            ]
        },
        {
            "action": "move c from table to a",
            "preconds": [
                "Espaço vazio em C",
                "Espaço vazio em A",
                " C sobre a bancada"
            ],
            "add": [
                "c on a"
            ],
            "delete": [
                " C sobre a bancada",
                "Espaço vazio em A"
            ]
        },
        {
            "action": "move c from a to table",
            "preconds": [
                "Espaço vazio em C",
                "espaço na bancada",
                "c on a"
            ],
            "add": [
                " C sobre a bancada",
                "Espaço vazio em A"
            ],
            "delete": [
                "c on a"
            ]
        },
        {
            "action": "move c from b to a",
            "preconds": [
                "Espaço vazio em C",
                "Espaço vazio em A",
                "bloco C no espaço B"
            ],
            "add": [
                "c on a",
                "Espaço vazio em B"
            ],
            "delete": [
                "bloco C no espaço B",
                "Espaço vazio em A"
            ]
        },
        {
            "action": "Move C da bancada para B",
            "preconds": [
                "Espaço vazio em C",
                "Espaço vazio em B",
                " C sobre a bancada"
            ],
            "add": [
                "bloco C no espaço B"
            ],
            "delete": [
                " C sobre a bancada",
                "Espaço vazio em B"
            ]
        },
        {
            "action": "move c from b to table",
            "preconds": [
                "Espaço vazio em C",
                "espaço na bancada",
                "bloco C no espaço B"
            ],
            "add": [
                " C sobre a bancada",
                "Espaço vazio em B"
            ],
            "delete": [
                "bloco C no espaço B"
            ]
        }
    ]
}

def main():
    start = problem['init']
    finish = problem['finish']
    ops = problem['ops']
    for action in gps(start, finish, ops):
        print (action)

if __name__ == '__main__':
    main()
