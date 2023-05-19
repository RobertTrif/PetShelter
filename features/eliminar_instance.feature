Feature: Eliminar gato

  Background:
    Given Exists a worker "worker1" with password "Hello67"
  
    Scenario: Create a Centro
        Given I login as worker "worker1" with password "Hello67"
        When I register a center
           | nombre   | direccion  | 
           | centro_2 | direccio_2 |
        Then I'm viewing a message "Centro creado correctamente"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Centro" from "Eliminar animal"
        Then I should delete de animal "centro_2"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Centro" from "Eliminar animal"


    Scenario: Create a Otro
        Given I login as worker "worker1" with password "Hello67"
       When I register a "otro"
            | nombre    | peso | color  | raza | pelaje | centro      |
            | Sebastian | 500  | Marron | Oso  | Largo  | centro_otro |    
        Then I'm viewing a message "Animal creado correctamente"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Otro" from "Eliminar animal"
        Then I should delete de animal "Sebastian"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Otro" from "Eliminar animal"

    Scenario: Create a cat
        Given I login as worker "worker1" with password "Hello67"
        When I register a "gato"
            | nombre | peso | color   | raza    | pelaje | centro      |
            | Michi  | 5    | Marron  | Abisino | corto  | centrogato |
        Then I'm viewing a message "Animal creado correctamente"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Gato" from "Eliminar animal"
        Then I should delete de animal "Michi"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Gato" from "Eliminar animal"


    Scenario: Create a Perro
        Given I login as worker "worker1" with password "Hello67"
       When I register a "perro"
            | nombre | peso | color | raza   | pelaje | centro       |
            | Rufus  | 40   | Beix  | Golden | largo  | centro_perro |
        Then I'm viewing a message "Animal creado correctamente"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Perro" from "Eliminar animal"
        Then I should delete de animal "Rufus"
        When I click on the "Administracion" button
        Then I should be redirected to the "Administracion" page
        When I select "Perro" from "Eliminar animal"

