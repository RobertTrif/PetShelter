Feature: Create instances
workers will have to be able to create new instances
    
    Background: There is a worker user
        Given Exists a worker "username" with password "password"

    Scenario: Register a cat 
    Given I login as worker "user" with password "password"
    When I register a cat
        | Nombre | Peso | Color | Raza   | Pelaje |
        | Gato   | 5    | Blanco| Europeo| Corto  |