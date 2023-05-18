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
        And go site and click the modify button
        When I Modify a center
            | nombre   | direccion  | 
            | centro_Modificado2 | direccio_Modificado2 |
        And I'm viewing the details of this center
            | nombre   | direccion  | 
            | centro_Modificado2 | direccio_Modificado2 |
