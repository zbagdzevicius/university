package first.second.third.beans.response;

import first.second.third.beans.documents.Datafiles;
import org.bson.types.Binary;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.constraints.NotNull;
import java.io.File;
import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.Date;

public class DatafilesResponse implements Serializable {
    private String id;
    private String timeStamp;
    private String userName;
    private Binary file;
    private String fileName;
    private String contentType;
    private String faculty;
    private String subject;

    public DatafilesResponse (Datafiles datafiles) {

        this.id = datafiles.getId();
        this.timeStamp = datafiles.getTimeStamp();
        this.userName = datafiles.getUserName();
        this.file = datafiles.getFile();
        this.fileName = datafiles.getFileName();
        this.contentType = datafiles.getContentType();
        this.faculty = datafiles.getFaculty();
        this.subject = datafiles.getSubject();

    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String String() {
        return timeStamp;
    }

    public void setTimeStamp(String timeStamp) {
        this.timeStamp = timeStamp;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public Binary getFile() {
        return file;
    }

    public void setFile(Binary file) {
        this.file = file;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public String getFaculty() {
        return faculty;
    }

    public void setFaculty(String faculty) {
        this.faculty = faculty;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getContentType() {
        return contentType;
    }

    public void setContentType(String contentType) {
        this.contentType = contentType;
    }
}
