import pkg_resources

# Get a list of all installed packages and their versions
installed_packages = pkg_resources.working_set

# Write the name and version of each package to a text file
with open("dependencies.txt", "w") as file:
    for package in installed_packages:
        file.write(f"{package.key}=={package.version}\n")

print("Dependencies written to dependencies.txt file.")
