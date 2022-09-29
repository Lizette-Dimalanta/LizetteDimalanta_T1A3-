from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ["Item", "Quantity", "Description"]
x.add_row(["Match", 1, "It has one match left."])
x.add_row(["Aconitum", 1, "Flowering plant belonging to the family Ranunculaceae."])
x.add_row(["Lucanidae", 1, "Also known as Phylum Arthropoda."])
x.add_row(["Asteraceae", 1, "The fair-maid-of-France."])
x.add_row(["Nightshade", 1, "The Solanaceae."])
x.add_row(["Chanterelle", 1, "Found in mossy coniferous forests."])

print(x)

# rack = { "Aconitum", "Chanterelle" }
# drawers = { "Lucanidae", "Asteraceae" }
# jars = { "Cerambycidae", "Nightshade" }

# recipe_1 = { "Aconitum" : "Vials", "Lucanidae" : "Drawers", "Cerambycidae" : "Jars"}
# recipe_2 = { "Asteraceae" : "Drawers", "Nightshade" : "Jars", "Chanterelle" : "Vials"}