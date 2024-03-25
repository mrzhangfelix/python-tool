import os
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
# from docx.opc.parts.image import ImagePart

def print_relationships(doc):
    for rel in doc.part.rels.values():
        print(f"Relationship Type: {rel.reltype}")

        print(f"Target Reference: {rel.target_ref}")

        print(f"Target Part: {rel.target_part}")

        print(f"Is External: {rel.is_external}")

        print("---")


def save_attachments_from_docx(docx_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = Document(docx_path)

    for rel in doc.part.rels.values():
        if rel.reltype == RT.IMAGE:
            # 通常，图片不被视为“附件”，但如果你也想保存它们，可以取消注释以下代码
            image_part = rel.target_part
            image_data = image_part.blob
            with open(os.path.join(output_dir, image_part.filename), 'wb') as f:
                f.write(image_data)
            pass
        elif rel.reltype.endswith('attachment'):
            attachment_part = rel.target_part
            attachment_data = attachment_part.blob
            filename = os.path.basename(rel.target_ref)
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(attachment_data)
                print(f"Saved attachment: {filename}")
        elif rel.reltype.endswith('oleObject'):
            attachment_part = rel.target_part
            attachment_data = attachment_part.blob
            filename = os.path.basename(rel.target_ref).replace(".bin", ".xlsx")
            with open(os.path.join(output_dir, filename), 'wb') as f:
                f.write(attachment_data)
                print(f"Saved attachment: {filename}")


docx_file_path = 'result.docx'  # 替换为你的 .docx 文件路径
output_directory = 'output'  # 替换为你想要保存附件的目录路径
doc = Document(docx_file_path)
# print_relationships(doc)
save_attachments_from_docx(docx_file_path, output_directory)