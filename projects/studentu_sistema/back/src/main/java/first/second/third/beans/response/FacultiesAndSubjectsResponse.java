package first.second.third.beans.response;

import first.second.third.beans.documents.FacultiesAndSubjects;

import java.io.Serializable;

public class FacultiesAndSubjectsResponse implements Serializable {

    //Data already had entity names set
    private String id;
    private String faculty;
    private String subject;
    private String university;

    public FacultiesAndSubjectsResponse(FacultiesAndSubjects facultiesAndSubjects){

        this.id = facultiesAndSubjects.getId();
        this.faculty = facultiesAndSubjects.getFaculty();
        this.subject = facultiesAndSubjects.getSubject();
        this.university = facultiesAndSubjects.getUniversity();
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public void setSubject(String subject) { this.subject = subject;
    }

    public String getUniversity() {
        return university;
    }

    public void setUniversity(String university) {
        this.university = university;
    }
}
