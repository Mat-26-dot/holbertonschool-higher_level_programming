def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print(f"Error: Invalid type for template. Expected str, got {type(template).__name__}")
        return
    if not (isinstance(attendees, list) and all(isinstance(item, dict) for item in attendees)):
        print(f"Error: Invalid type for attendees. Expected list of dicts, got {type(attendees).__name__}")
        return
    
    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    # Handle empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    placeholders = ["name", "event_title", "event_date", "event_location"]
    
    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        output_text = template
        
    # Replace missing data with "N/A"
    for ph in placeholders:
        value = attendee.get(ph, "N/A")
        output_text = output_text.replace(f"{{{{{ph}}}}}", str(value))
        
        filename = f"output_{idx}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(output_text)
        
        # Write to output file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(output_text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
