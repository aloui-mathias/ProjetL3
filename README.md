Membres du projet:
ALOUI Mathias
BADAGBON Jacques
BERTIN-JOHANNET Roland
POVEDA Maxime
RAHNI Dyhia

Matériel nécéssaire: Logiciel blender, python 3.4.0 .

Pour lancer le programme:

Il suffit d'ouvrir le fichier Main.blend dans le logiciel Blender, choisir la taille désirée du labyrinthe dans l'argument de la fonction generate_maze() au bas du script, qui lorsque vous ouvrez le fichier est 3 par défaut et de cliquez sur "Run Script" en haut à droite de l'espace "Text Editor". Vous pourrez visualiser l'objet généré dans la partie "3D viewport" de Blender.

Fonctions:

bpy.ops.mesh.primitive_cube_add(location=(x, y, z)) prend en argument un triplet location qui génère un cube aux coordonnées x, y et z.

bpy.ops.transform.resize(value=(z, y, z)) prend en argument un triplet value qui modifie les dimensions tridimensionelles de l'objet sélectionné. Si elle est effectué à la suite de bpy.ops.mesh.primitive_cube_add(location=(x, y, z)) l'object sélectionné est celui généré précedemment.

v_wall(x, y, z) prend en argument 3 décimaux et génère un mur vertical au coordonnées correspondantes x, y et z.

h_wall(x, y, z) prend en argument 3 décimaux et génère un mur horizontal au coordonnéescorrespondantes x, y et z.

delete_All() ne prend pas d'argument et permet de supprimer tout les objet de l'espace. Elle est nécéssaire pour vider l'espace d'édition entre chaque execution car cela ne se fait pas automatiquement.

generate_v_walls(m, k) prend en argument la matrice des murs verticaux d'un étage et un décimal et génère les murs verticaux correspondant à la hauteur du décimal k.

generate_h_walls(m, k) prend en argument la matrice des murs horizontaux d'un étage et un décimal et génère les murs verticaux correspondant à la hauteur du décimal k.

generate_entrances(size, k) prend en argument un entier et un décimal et génère les entré d'étage pour le cube.

generate_floors(size, k, point, holes) prend en argument un entier, un décimal, un entier et une matrice qui contient les coordonnées des trous de tout les étages et génère les passages entres demi-étage.

generate_cube(maze) prend en argument un maze et génère le labyrinthe correspondant.

generate_maze(size) prend en arugment un entier et génère un labyrinthe de la taille size.
