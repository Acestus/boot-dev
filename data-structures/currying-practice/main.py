def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.split("\n")
            num_lines = 0
            for line in lines:
                if sequence in line:
                    num_lines += 1
            return num_lines

        return with_length

    return with_char
