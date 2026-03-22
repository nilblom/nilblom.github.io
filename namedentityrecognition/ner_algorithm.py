def find_named_entities(tokens):
    entities = []
    sentence_end = ['.', '!', '?']
    sentence_start = ['“']
    exclude_words = ["I"]
    entity_length_limit = 9
    bind_words = ["of"]
    i = 0
    while i < len(tokens):
        if i == 0 or (tokens[i-1] in sentence_end) or (tokens[i-1] in sentence_start):
            pass
        elif tokens[i][0].isupper() and tokens[i] not in exclude_words:
            j = i

            while j >= 0 and (j > i-entity_length_limit) and (tokens[j][0].isupper() or tokens[j] in bind_words):
                j -= 1
            if tokens[j+1] in bind_words:
	            j += 1

            k = 0
            while k < len(entities):
                if entities[k][0] == j+1:
                    entities.pop(-1)
                k += 1

            entities.append((j+1, i))
        i += 1
    return entities

entities = find_named_entities(tokens)
for i, j in entities:
    for n in range(i, j+1):
        print(tokens[n], end=" ")
    print()
