import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern():
    """Generate a procedural pattern of objects using nested loops.

    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
    # --- Configuration variables ---
    num_rows = 5        # Number of rows in the pattern.
    num_cols = 5        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.

    for row in range(num_rows):
        for col in range(num_cols):
            x_pos = col * spacing
            z_pos = row * spacing
            wizard_height = 15.0*row*col
            if (row + col) % 2 == 0:
                wizard_cube = cmds.polyCube(
                name=f"wizard_cube_{row}_{col}",
                width=2.0,
                height=wizard_height,
                depth=2.0)[0]
                
                cmds.move(x_pos,wizard_height/2.0,z_pos,wizard_cube)
            else:
                wizard_pyramid = cmds.polyPyramid(
                name=f"wizard_pyramid_{row}_{col}",
                subdivisionsCaps=4,
                subdivisionsHeight=4,
                numberOfSides=4
                )[0]
                pyramid_height = cmds.getAttr(wizard_pyramid+".scaleY")
                cmds.move(x_pos, pyramid_height/2.0,z_pos)


# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
print("Pattern generated successfully!")
