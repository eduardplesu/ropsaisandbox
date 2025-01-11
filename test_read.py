import asyncio
from modules.document_intelligence_read import analyze_document_read

async def test_read():
    with open("sample.pdf", "rb") as f:  # Replace with a valid file path
        document_bytes = f.read()

    result = await analyze_document_read(document_bytes)
    print("Extracted Text:", result)

if __name__ == "__main__":
    asyncio.run(test_read())
