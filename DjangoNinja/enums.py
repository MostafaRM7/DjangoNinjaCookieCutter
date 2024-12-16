

class FileFormat:
    jpeg = "image/jpeg"
    png = "image/png"
    gif = "image/gif"
    pdf = "application/pdf"
    docx = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    doc = "application/msword"
    txt = "text/plain"
    csv = "text/csv"
    xlsx = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    xls = "application/vnd.ms-excel"
    mp4 = "video/mp4"
    mkv = "video/x-matroska"
    avi = "video/x-msvideo"
    mov = "video/quicktime"
    mp3 = "audio/mpeg"
    wav = "audio/wav"
    aac = "audio/aac"
    flac = "audio/flac"
    ogg = "audio/ogg"
    webm = "audio/webm"
    zip = "application/zip"
    rar = "application/vnd.rar"
    tar = "application/x-tar"
    gz = "application/gzip"

    def video(self) -> tuple:
        return self.mp4, self.mkv, self.avi, self.mov

    def audio(self) -> tuple:
        return self.mp3, self.wav, self.aac, self.flac, self.ogg, self.webm

    def image(self) -> tuple:
        return self.jpeg, self.png, self.gif

    def document(self) -> tuple:
        return self.pdf, self.docx, self.doc, self.txt, self.csv, self.xlsx, self.xls

    def archive(self) -> tuple:
        return self.zip, self.rar, self.tar, self.gz

    def text(self) -> tuple:
        return (self.txt,)
