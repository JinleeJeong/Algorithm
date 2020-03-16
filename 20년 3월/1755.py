string = input()

stringList = string.split(".")


if stringList[1] == "dib":
    print("Paint.Picture")
elif stringList[1] == "doc":
    print("Word.Document.8")
elif stringList[1] == "docx":
    print("Word.Document.12")
elif stringList[1] == "htm":
    print("htmfile")
elif stringList[1] == "html":
    print("htmlfile")
elif stringList[1] == "hwp":
    print("Hwp.Document.96")
elif stringList[1] == "hwpx":
    print("Hwp.Document.hwpx.96")
elif stringList[1] == "hwt":
    print("Hwp.Document.hwt.96")
elif stringList[1] == "jpe":
    print("jpegfile")
elif stringList[1] == "jpeg":
    print("jpegfile")
elif stringList[1] == "jpg":
    print("jpegfile")
elif stringList[1] == "ppt":
    print("PowerPoint.Show.8")
elif stringList[1] == "pptx":
    print("PowerPoint.Show.12")
else:
    print("powerpointxmlfile")