Feature: Eliminar gato

  Background:
    Given Exists a worker "worker1_" with password "Hello67_"

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
            
  Scenario: Eliminar un gato
    Given I login as worker "worker1_" with password "Hello67_"
    When I click on the "Administracion" button
    Then I should be redirected to the "Administracion" page
    When I select "Gato" from "Eliminar animal"
    Then I should delete de animal "nuevo gato"
    
  Scenario: Eliminar un perro
    Given I login as worker "worker1_" with password "Hello67_"
    When I click on the "Administracion" button
    Then I should be redirected to the "Administracion" page
    When I select "Perro" from "Eliminar animal"
    Then I should delete de animal "rufus"

    Scenario: Eliminar un otro
    Given I login as worker "worker1_" with password "Hello67_"
    When I click on the "Administracion" button
    Then I should be redirected to the "Administracion" page
    When I select "Otro" from "Eliminar animal"
    Then I wait for 16 seconds
    Then I should delete de animal "sebastian"      