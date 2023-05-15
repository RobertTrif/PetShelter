Feature: Create instances
    workers will have to be able to create new instances
    
    Background: There is a registered worker
        Given Exists a worker "worker1_" with password "Hello67_"

    Scenario: Create a center
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a center
            | nombre   | direccion  | 
            | centro_2 | direccio_2 |
        Then I'm viewing a message "Centro creado correctamente"
        And I'm viewing the details of this center
            | nombre   | direccion  | 
            | centro_2 | direccio_2 |      

    Scenario: Create a cat
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a "gato"
            | nombre | peso | color   | raza    | pelaje | centro      |
            | Michi  | 5    | Marron  | Abisino | corto  | centro_gato |
        Then I'm viewing a message "Animal creado correctamente"
        And I'm viewing the page details for this "Gato"
            | nombre | peso | color   | raza    | pelaje | centro      |
            | Michi  | 5    | Marron  | Abisino | corto  | centro_gato |
    
    Scenario: Create a dog
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a "perro"
            | nombre | peso | color | raza   | pelaje | centro       |
            | Rufus  | 40   | Beix  | Golden | largo  | centro_perro |
        Then I'm viewing a message "Animal creado correctamente"
        And I'm viewing the page details for this "Perro"
            | nombre | peso | color | raza   | pelaje | centro       |
            | Rufus  | 40   | Beix  | Golden | largo  | centro_perro |
    
    Scenario: Create other
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a "otro"
            | nombre    | peso | color  | raza | pelaje | centro      |
            | Sebastian | 500  | Marron | Oso  | Largo  | centro_otro |
        Then I'm viewing a message "Animal creado correctamente"
        And I'm viewing the page details for this "Otro"
            | nombre    | peso | color  | raza | pelaje | centro      |
            | Sebastian | 500  | Marron | Oso  | Largo  | centro_otro |

    Scenario: Try to register a cat but not logged in
    Given I'm not logged in
    When I register a "gato"
        | nombre | peso | color   | raza    | pelaje | centro      |
        | Michi  | 5    | Marron  | Abisino | corto  | centro_gato |
    Then I'm viewing a message "Para acceder a esta seccion necesitas iniciar sesion con tu cuenta de trabajdor del centro"
    And There are 0 cats