text = "hello"
symbols = "==="
new_symbols = "***"

def wrap_text (text, symbols):
    result = symbols + text + symbols
    return result

# result = wrap_text(text, symbols)
# print(result)

#Part 2

result = wrap_text(text,symbols)
result2 = wrap_text(result,new_symbols)

print(result2)
