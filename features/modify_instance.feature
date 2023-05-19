Feature: Modify instances
    workers will have to be able to modificate instances

    Background: There is a registered worker
        Given Exists a worker "worker1_" with password "Hello67_"
    
     Scenario: Modify a center
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a center
            | nombre   | direccion  | 
            | centro_2 | direccio_2 |
        Then I'm viewing a message "Centro creado correctamente"
        And I'm viewing the details of this center
            | nombre   | direccion  | 
            | centro_2 | direccio_2 |     
        And Go site and click the modify centro button
        When I Modify a center
            | nombre   | direccion  | 
            | centro_Modificado2 | direccio_Modificado2 |
        And I'm viewing the details of this center
            | nombre   | direccion  | 
            | centro_Modificado2 | direccio_Modificado2 |

    Scenario: Modify a cat
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a "gato"
            | nombre | peso | color   | raza    | pelaje | centro      |
            | Michi  | 5    | Marron  | Abisino | corto  | centro_gato |
        Then I'm viewing a message "Animal creado correctamente"
        And I'm viewing the page details for this "Gato"
            | nombre | peso | color   | raza    | pelaje | centro      |
            | Michi  | 5    | Marron  | Abisino | corto  | centro_gato |        
        And Go site and click the modify cat button
        When I Modify a cat
            | nombre | peso | color   | raza    | pelaje |
            | MichiLini  | 15    | Marron  | Abisino | Largo  |
        And I'm viewing the page details for this after modify "Gato"
            | nombre | peso | color   | raza    | pelaje | centro      |
            | MichiLini  | 15    | Marron  | Abisino | Largo  | centro_gato |  
    
    Scenario: Modify a dog
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a "perro"
            | nombre | peso | color | raza   | pelaje | centro       |
            | Rufus  | 40   | Beix  | Golden | largo  | centro_perro |
        Then I'm viewing a message "Animal creado correctamente"
        And I'm viewing the page details for this "Perro"
            | nombre | peso | color | raza   | pelaje | centro       |
            | Rufus  | 40   | Beix  | Golden | largo  | centro_perro |
        And Go site and click the modify dog button
        When I modify a dog
            | nombre | peso | color |
            | RufusMix  | 20   | Negro  |
         And I'm viewing the page details for this after modify "Perro"
            | nombre | peso | color | raza   | pelaje | centro       |
            | RufusMix  | 20   | Negro  | Golden | largo  | centro_perro |

    Scenario: Modify a other
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a "otro"
            | nombre    | peso | color  | raza | pelaje | centro      |
            | Sebastian | 500  | Marron | Oso  | Largo  | centro_otro |
        Then I'm viewing a message "Animal creado correctamente"
        And I'm viewing the page details for this "Otro"
            | nombre    | peso | color  | raza | pelaje | centro      |
            | Sebastian | 500  | Marron | Oso  | Largo  | centro_otro |
        And Go site and click the modify other button
        When I modify a other
            | nombre    | peso | color  | raza | pelaje |
            | Osito | 200  | Marron | Oso  | Largo  |
        And I'm viewing the page details for this after modify "Otro"
            | nombre    | peso | color  | raza | pelaje | centro      |
            | Osito | 200  | Marron | Oso  | Largo  | centro_otro |
    
    Scenario: Modify a user
        Given I login as worker "worker1_" with password "Hello67_"
        And Go site and click the modify user button
        When I modify a user
            | nombre | apellidos | telefono | email |
            | Osito | Amoroso | 123456777 | random@gmail.com |
        And I'm viewing the page details for this after modify a user
            | nombre | apellidos |
            | Osito | Amoroso |