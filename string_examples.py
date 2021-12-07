s1 = "spam\n"   # single-delimited
s2 = 'spam\n'
s3 = """spam\n"""  # triple-delimited
s4 = '''spam\n'''  # \n \r \t \f \b
s5 = r"spam\n"   # raw string

print(len(s1), len(s5))
print("Python's a great language")
print('Python is a "great" language')
print("Python's a \"great\" language")
print("""Python's a "great" language""")
print(r"Help me! \\o//")
print(r"\r\n\t\b\f")
print("\r\n\t\b\f")

