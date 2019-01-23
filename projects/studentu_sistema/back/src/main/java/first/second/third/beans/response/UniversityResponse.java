package first.second.third.beans.response;

import first.second.third.beans.documents.FacultiesAndSubjects;

import java.io.Serializable;

public class UniversityResponse implements Serializable {

    private String university;

    public UniversityResponse(FacultiesAndSubjects facultiesAndSubjects){
        this.university = facultiesAndSubjects.getUniversity();
    }

    public String getUniversity() {
        return university;
    }

    public void setUniversity(String university) {
        this.university = university;
    }
}
