

    # Update the index.md file
    with open(INDEX_FILE, 'a', encoding='utf-8') as index_file:
        index_file.write(f"- [{contrib_name}]({os.path.basename(markdown_file)})\n")

    print(f"Updated index file: {INDEX_FILE}")
