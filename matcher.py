import sys
import io

def load_predefined_words(filename):
    with open(filename, 'r') as f:
        return set(word.strip().lower() for word in f)


SSIZE_MAX = 2**30  # 1 GB, conservative estimate of max size of a read on POSIX systems

def process_file(input_filename, predefined_words, chunk_size=2**20):
    matches = {}
    with open(input_filename, 'r') as f:
        for line_number, line in enumerate(f, 1):
            #print('=======================')
            #print(line_number, line)
            line_io = io.StringIO(line.lower())
            partial_word = ""
            while True:
                current_chunk_size = min(chunk_size, SSIZE_MAX)
                chunk = line_io.read(current_chunk_size)
                if not chunk:
                    break
                
                # Combine with any partial word from the previous chunk
                chunk = partial_word + chunk
                words = chunk.split()
                
                # Check if the last word is complete
                if line_io.tell() < len(line) and not chunk.endswith(' '):
                    #print('incomplete chunk')
                    #print('partial word', words[-1])
                    partial_word = words[-1]
                    words = words[:-1]
                else:
                    partial_word = ""
                
                for word in words:
                    if word in predefined_words:
                        if word not in matches:
                            matches[word] = []
                        if line_number not in matches[word]:
                            matches[word].append(line_number)
            
            # Process any remaining partial word
            if partial_word and partial_word in predefined_words:
                if partial_word not in matches:
                    matches[partial_word] = []
                if line_number not in matches[partial_word]:
                    matches[partial_word].append(line_number)
    
    return matches

def main(input_filename, predefined_words_filename):
    predefined_words = load_predefined_words(predefined_words_filename)
    matches = process_file(input_filename, predefined_words)
    
    for word, line_numbers in matches.items():
        print(f"Word: {word}")
        print(f"Found on lines: {', '.join(map(str, line_numbers))}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python matcher.py <input_file> <predefined_words_file>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    predefined_words_filename = sys.argv[2]
    main(input_filename, predefined_words_filename)