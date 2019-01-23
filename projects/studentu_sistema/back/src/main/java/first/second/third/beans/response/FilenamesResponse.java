package first.second.third.beans.response;

import first.second.third.beans.documents.Datafiles;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.Date;

public class FilenamesResponse implements Serializable {
    private String timeStamp;
    private String userName;
    private String fileName;

    public FilenamesResponse (Datafiles datafiles) {

        this.timeStamp = datafiles.getTimeStamp();
        this.userName = datafiles.getUserName();
        this.fileName = datafiles.getFileName();

    }

    public String getTimeStamp() {
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

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }
}
