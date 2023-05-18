Feature: Modify instances
    workers will have to be able to modificate instances

    Background: There is a registered worker
        Given Exists a worker "worker1_" with password "Hello67_"
    
     Scenario: Modify centro
        Given I login as worker "worker1_" with password "Hello67_"
        When I register a center
            | nombre   | direccion  | 
            | centro_2 | direccio_2 |
        When go site and click the modify button
