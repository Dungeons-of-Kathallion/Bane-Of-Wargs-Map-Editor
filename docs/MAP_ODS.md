## Introduction

After reading this documentation, you'll be able to fully understand the work of the Bane Of Wargs Map Editor and how to edit the `map.ods` file properly. Please, read the [map point documentation](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/wiki/Creating-Map-Points) before reading this document.

### Map.ods' work

As you may know, in a map point definition there;s multiple 'attributes'. In the map.ods file, each map point is represented by a cell. Each sheets represent a map point attribute. To modify these attributes, you'll need to enter things in these cells.

Note that it's recommended to highlight different cells by map zones. For example in the vanilla map, Stall Fields are highlighted in bright yellow.

#### Sheets // X

This sheet represents every point x coordinates attribute.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/b8aacf39-9e5c-4a28-aa12-65839ad347fa)

**This sheet should not be modified.**

#### Sheets // Y

This sheet represents every point y coordinates attribute.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/def75806-cffa-4269-8dcb-c6401c60849d)

**This sheet should not be modified.**

#### Sheets // Map Zone

This sheet represents every map zone attribute of the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/93565ba2-b0bf-4c3e-a552-d89e0f1a95f8)

**Here you'll enter a single string: the name of the map zone**

#### Sheets // Blocked

This sheet represents every map point blocked directions.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/dd5ad5f5-8abd-48a7-a831-913a738caca9)

**Here you'll enter blocked directions separated by a comma and a single space after.**

#### Sheets // Items

This sheet represents every ground items at the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/82dde0c9-8c2f-46fe-bb96-2f309f0c7522)

**Here you'll enter ground items names separated by a comma and a single space after.**

#### Sheets // Enemies

This sheet represents the number of enemies that will spawn at the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/6e89743b-bdb8-4b7b-accc-b48ccb9dd126)

**Here you'll enter an integer representing the number of spawning enemies.**

#### Sheets // Enemy Type

This sheet represents the enemy category that will spawn at the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/93d7955f-5c1f-450c-a79b-2a4157c8afbc)

**Here you'll enter the name of the enemy category.**

#### Sheets // Dialogs

This sheet represents the dialog that will display at the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/d5b9e7de-bc83-4b8c-9de9-e324915fc176)

**Here you'll enter the name of the dialog.**

#### Sheets // NPCS

This sheet represents the list of npcs that will be met at the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/52948122-a9d1-4e36-a0de-fac31acd9cdb)

**Here you'll enter the list of the npcs names.**

#### Sheets // Keys

This sheet represents the keys that are required to go to the map point.
![image](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs/assets/87318892/7b4627e7-009d-41fd-8131-39f625be8337)

**Here you'll enter the required keys separated by a comma and you'll add `, <true | false>` at the end, depending on if you want to keys to be removed from the player inventory after the player has used them.**
