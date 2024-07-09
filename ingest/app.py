from unstructured_ingest import *


def main():
    collection_name="a1"
    print("started file reader...")
    raw_pdf_elements=file_reader()
   
    print("text_insert started...")
    text_insert(raw_pdf_elements)

    print("image_insert started...")
    last_indices=get_last_index_of_page(raw_pdf_elements)
    image_insert_with_text(raw_pdf_elements,last_indices)
    
    get_docummets()

    print("Raptor started...")
    raptor_texts = raptor()
    get_documents_with_raptor(raptor_texts)
    
    print("add data to postgres Started...")
    add_docs_to_postgres(collection_name)
    print("All Done...")

if __name__=="__main__":
    main()