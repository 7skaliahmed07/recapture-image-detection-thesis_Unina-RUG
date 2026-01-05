import os
import json

def combine_all_files():
    print("📁 Listing files in current directory...")
    
    # Get all files
    all_files = os.listdir('.')
    csv_files = sorted([f for f in all_files if f.lower().endswith('.csv')])
    json_files = sorted([f for f in all_files if f.lower().endswith('.json')])
    
    print(f"✅ Found {len(csv_files)} CSV files")
    print(f"✅ Found {len(json_files)} JSON files")
    
    # Create COMBINED CSV DATA file
    print("\n📝 Creating 'COMBINED_CSV_DATA.txt'...")
    with open('COMBINED_CSV_DATA.txt', 'w', encoding='utf-8') as out_file:
        out_file.write("=" * 80 + "\n")
        out_file.write("COMBINED CSV FILES DATA\n")
        out_file.write("=" * 80 + "\n\n")
        
        for csv_file in csv_files:
            out_file.write(f"📄 FILE: {csv_file}\n")
            out_file.write("-" * 60 + "\n")
            
            try:
                with open(csv_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Count lines
                out_file.write(f"Total lines: {len(lines)}\n\n")
                
                # Show all lines (or first 50 if too many)
                max_lines = 50
                if len(lines) <= max_lines:
                    for i, line in enumerate(lines):
                        out_file.write(line.rstrip() + "\n")
                else:
                    for i, line in enumerate(lines[:max_lines]):
                        out_file.write(line.rstrip() + "\n")
                    out_file.write(f"\n... and {len(lines)-max_lines} more lines\n")
                    
            except Exception as e:
                out_file.write(f"❌ Error reading file: {str(e)}\n")
            
            out_file.write("\n" + "=" * 80 + "\n\n")
    
    # Create COMBINED JSON DATA file
    print("📝 Creating 'COMBINED_JSON_DATA.txt'...")
    with open('COMBINED_JSON_DATA.txt', 'w', encoding='utf-8') as out_file:
        out_file.write("=" * 80 + "\n")
        out_file.write("COMBINED JSON FILES DATA\n")
        out_file.write("=" * 80 + "\n\n")
        
        for json_file in json_files:
            out_file.write(f"📄 FILE: {json_file}\n")
            out_file.write("-" * 60 + "\n")
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Try to parse and pretty print JSON
                try:
                    data = json.loads(content)
                    out_file.write(json.dumps(data, indent=2))
                except json.JSONDecodeError:
                    # If not valid JSON, show raw content
                    out_file.write("⚠️  Not valid JSON format, showing raw content:\n\n")
                    out_file.write(content)
                    
            except Exception as e:
                out_file.write(f"❌ Error reading file: {str(e)}\n")
            
            out_file.write("\n" + "=" * 80 + "\n\n")
    
    print("\n" + "✨" * 40)
    print("✅ SUCCESS! Created two files:")
    print(f"   1. 'COMBINED_CSV_DATA.txt' - Contains all {len(csv_files)} CSV files")
    print(f"   2. 'COMBINED_JSON_DATA.txt' - Contains all {len(json_files)} JSON files")
    print("✨" * 40)

# Run the script
if __name__ == "__main__":
    combine_all_files()