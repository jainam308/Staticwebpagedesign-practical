for i in range(1, 22):  # Creating 21 HTML files
    filename = f"Practical-{i}.html"
    with open(filename, "w") as f:
        f.write(f"<!DOCTYPE html>\n<html>\n<head>\n    <title>Practical {i}</title>\n</head>\n<body>\n    <h1>Practical {i}</h1>\n    <p>This is the content of Practical {i}.</p>\n</body>\n</html>")
    print(f"{filename} created.")
