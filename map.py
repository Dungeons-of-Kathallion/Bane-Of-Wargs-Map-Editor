import yaml
from pyexcel_ods import get_data
from rich.progress import Progress

try:
    # Get map calc data
    data = get_data("map.ods")

    # Ask user path of the yaml file where the
    # data should be stored
    print('''
████████████████████████████████████████████████████████████████████▀███████
█▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─▄▄─███─▄▄─█▄─▄▄─███▄─█▀▀▀█─▄██▀▄─██▄─▄▄▀█─▄▄▄▄█─▄▄▄▄█
██─▄─▀██─▀─███─█▄▀─███─▄█▀███─██─██─▄██████─█─█─█─███─▀─███─▄─▄█─██▄─█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▄▄▄▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    ''')
    which_file = input("Please enter the path to your yaml file: ")
    print(f"\nGenerating {which_file} data...")

    with Progress() as progress:
        task1 = progress.add_task("[red]Loading .ods File...", total=None)
        task2 = progress.add_task("[red]Creating Map Data...", total=100)
        task3 = progress.add_task("[red]Parsing Map Data...", total=100)
        task4 = progress.add_task("[red]Dumping Map Data...", total=None)
        # Open map.yaml file and save its data to
        # a variable called map
        with open('out/map.yaml', 'r') as f:
            map = yaml.safe_load(f)
        progress.update(task1, total=1, advance=1)

        # Create required variables
        count = 0
        count_point = 0
        count_point2 = 0
        y_count = 64
        x_count = -64
        map_zone_name = None
        blocked_directions = None
        ground_items = None
        enemies_num = None
        enemies_type = None
        dialog = None
        npc_names = None
        keys = None
        cont = True

        while cont:
            cont = False
            # Loop to get every map point
            for counting in range(0, 16641):
                progress.update(task2, advance=.01)
                # Resetting stuff
                if count_point2 == 129:
                    count_point += 1
                    count_point2 = 0
                if x_count == 65:
                    x_count = -64
                    y_count -= 1


                # Get map point map zone
                if data["Map Zone"][count_point][count_point2] != None:
                    map_zone_name = str(data["Map Zone"][count_point][count_point2]).replace("\u2019", "'")
                else:
                    map_zone_name = None


                # Map point blocked directions
                # Get map point blocked directions
                if data["Blocked"][count_point][count_point2] != None:
                    blocked_directions = str(data["Blocked"][count_point][count_point2])
                else:
                    blocked_directions = None

                # Create the blocked directions correct list
                blocked_directions = "".join(blocked_directions.split(','))
                blocked_directions = blocked_directions.split()

                # Map point npcs
                # Get map point npcs
                if data["NPCS"][count_point][count_point2] != None:
                    npc_names = str(data["NPCS"][count_point][count_point2])
                else:
                    npc_names = None

                # Create the npcs correct list
                npc_names = npc_names.split(', ')


                # Map point keys
                # Get map point keys
                if data["Keys"][count_point][count_point2] != None:
                    keys = str(data["Keys"][count_point][count_point2])
                else:
                    keys = None

                # Create the keys correct list
                if keys != 'None':
                    keys = keys.split(', ')
                    remove_keys = keys[len(keys) - 1]
                    if remove_keys == 'False':
                        remove_keys = False
                    elif remove_keys == 'True':
                        remove_keys = True
                    del keys[len(keys) - 1]

                    keys = {
                        "required keys": keys,
                        "remove key": remove_keys
                    }


                # Map point ground items
                # Get map point ground items
                if data["Items"][count_point][count_point2] != None:
                    ground_items = str(data["Items"][count_point][count_point2])
                else:
                    ground_items = None

                # Create the ground items correct list
                ground_items = ground_items.split(', ')


                # Get map point enemies number
                if data["Enemies"][count_point][count_point2] != None:
                    enemies_num = data["Enemies"][count_point][count_point2]
                    enemies_type = data["Enemy Type"][count_point][count_point2]
                else:
                    enemies_num = None


                # Get map point dialog
                if data["Dialogs"][count_point][count_point2] != None:
                    dialog = data["Dialogs"][count_point][count_point2]
                else:
                    dialog = None

                # Create new map point dictionary
                if enemies_num == 'None' and dialog == 'None' and keys == 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions
                    }
                if dialog == 'None' and enemies_num != 'None' and keys == 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type
                    }
                if dialog != 'None' and enemies_num == 'None' and keys == 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog
                    }
                if dialog != 'None' and enemies_num != 'None' and keys == 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog
                    }
                if dialog == 'None' and enemies_num != 'None' and keys != 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "key": keys
                    }
                if dialog != 'None' and enemies_num == 'None' and keys != 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "key": keys
                    }
                if dialog != 'None' and enemies_num != 'None' and keys != 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "key": keys
                    }
                if enemies_num == 'None' and dialog == 'None' and keys != 'None' and npc_names == ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "key": keys
                    }
                if enemies_num == 'None' and dialog == 'None' and keys == 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "npc": npc_names
                    }
                if dialog == 'None' and enemies_num != 'None' and keys == 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "npc": npc_names
                    }
                if dialog != 'None' and enemies_num == 'None' and keys == 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "npc": npc_names
                    }
                if dialog != 'None' and enemies_num != 'None' and keys == 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "npc": npc_names
                    }
                if dialog == 'None' and enemies_num != 'None' and keys != 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "key": keys,
                        "npc": npc_names
                    }
                if dialog != 'None' and enemies_num == 'None' and keys != 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "key": keys,
                        "npc": npc_names
                    }
                if dialog != 'None' and enemies_num != 'None' and keys != 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "key": keys,
                        "npc": npc_names
                    }
                if enemies_num == 'None' and dialog == 'None' and keys != 'None' and npc_names != ['None'] and ground_items == ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "key": keys,
                        "npc": npc_names
                    }
                if enemies_num == 'None' and dialog == 'None' and keys == 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "item": ground_items
                    }
                if dialog == 'None' and enemies_num != 'None' and keys == 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num == 'None' and keys == 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num != 'None' and keys == 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "item": ground_items
                    }
                if dialog == 'None' and enemies_num != 'None' and keys != 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "key": keys,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num == 'None' and keys != 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "key": keys,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num != 'None' and keys != 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "key": keys,
                        "item": ground_items
                    }
                if enemies_num == 'None' and dialog == 'None' and keys != 'None' and npc_names == ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "key": keys,
                        "item": ground_items
                    }
                if enemies_num == 'None' and dialog == 'None' and keys == 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if dialog == 'None' and enemies_num != 'None' and keys == 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num == 'None' and keys == 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num != 'None' and keys == 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if dialog == 'None' and enemies_num != 'None' and keys != 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "key": keys,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num == 'None' and keys != 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "dialog": dialog,
                        "key": keys,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if dialog != 'None' and enemies_num != 'None' and keys != 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "enemy": enemies_num,
                        "enemy type": enemies_type,
                        "dialog": dialog,
                        "key": keys,
                        "npc": npc_names,
                        "item": ground_items
                    }
                if enemies_num == 'None' and dialog == 'None' and keys != 'None' and npc_names != ['None'] and ground_items != ['None']:
                    new_map_point = {
                        "x": x_count,
                        "y": y_count,
                        "map zone": map_zone_name,
                        "blocked": blocked_directions,
                        "key": keys,
                        "npc": npc_names,
                        "item": ground_items
                    }
                    
                # Update map dictionary and add the new map
                # point just loaded
                # If there is no map zone name, don't
                # create the map point for optimization
                # and delete the corresponding map point
                if map_zone_name != 'None':
                    map[f"point{count}"].update(new_map_point)
                else:
                    del map[f"point{count}"]
                # Required operations
                x_count += 1
                count_point2 += 1


                count += 1

        # Re-name map point names so they're all
        # in numerical order
        count = 0
        new_map = {}
        
        progress.update(task3, total=(len(list(map)) / 10))
        while count < len(list(map)):
            new_map[f"point{count}"] = map[str(list(map)[count])]
            progress.update(task3, advance=.1)
            
            count += 1
            
        progress.update(task3, advance=1)
            
        # Save numerically ordered map into
        # the real map
        map = new_map

        # Save created map data stored under map
        # variable to the real map.yaml file

        dumped = "# Copyright (c) 2024 by @Cromha\n#\n# This file was generated with the Bane Of Wargs Map Editor\n# https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs-Map-Edito\n#\n# Bane Of Wargs Editor is free software: you can redistribute it and/or modify it under the\n# terms of the GNU General Public License as published by the Free Software\n# Foundation, either version 3 of the License, or (at your option) any later version.\n#\n# Bane Of Wargs is distributed in the hope that it will be useful, but WITHOUT ANY\n# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A\n# PARTICULAR PURPOSE. See the GNU General Public License for more details.\n#\n# You should have received a copy of the GNU General Public License along with\n# this program. If not, see <https://www.gnu.org/licenses/>.\n\n"
        dumped += yaml.dump(map)

        with open(which_file, 'w') as f:
            f.write(dumped)
        progress.update(task4, total=1, advance=1)
# If an error occurred during the program
except Exception as error:
    print(f"ERROR: An error occurred when running the program: \n{error}")
