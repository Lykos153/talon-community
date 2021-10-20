double dash: "--"
triple quote: "'''"
#ellipses: "…"
ellipses: "..."
spam: ", "
coal gap: ": "
pipe gap: " | "
boom: ". "
arrow: "->"
dub arrow: "=>"
new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty round: "()"
empty square: "[]"
empty curly: "{}"
empty diamond: "<>"
empty quad: '""'
empty twin: "''"
empty escaped quad: '\\"\\"'
empty escaped twin: "\\'\\'"
empty escaped round: '\\(\\)'
tween <user.symbol_key>:
    '{symbol_key}{symbol_key}'
    key(left)
quad:
    '""'
    key(left)
twin:
    "''"
    key(left)
skis:
    '``'
    key(left)
escaped quad:
    '\\"\\"'
    key(left)
    key(left)
escaped twin:
    "\\'\\'"
    key(left)
    key(left)
round:
	insert("()")
	key(left)
escaped round:
    '\\(\\)'
    key(left)
    key(left)
square: 
	insert("[]") 
	key(left)
curly: 
	insert("{}") 
	key(left)
diamond: 
	insert("<>") 
	key(left)
(diamond | angle) that: 
    text = edit.selected_text()
    user.paste("<{text}>")
(curly | lace) that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
(round | leper) that: 
    text = edit.selected_text()
    user.paste("({text})")
(double | quad) that:
    text = edit.selected_text()
    user.paste("'{text}'")
(double quote | dubquote) that:
    text = edit.selected_text()
    user.paste('"{text}"')
(single | twin) that:
    text = edit.selected_text()
    user.paste("'{text}'")

slicer:
	edit.line_end()
	key(enter)
    insert("- ")

end gap:
    edit.line_end()
    key(space)

slider:
	edit.line_end()
	insert(",")
    key(enter)

breaker:
	edit.line_end()
	insert(" {")
    key(enter)

chronic:
	edit.line_end()
	insert(":")
    key(enter)
