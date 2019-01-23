package first.second.third.services;


import first.second.third.beans.documents.FacultiesAndSubjects;
import first.second.third.beans.response.FacultiesAndSubjectsResponse;
import first.second.third.beans.response.UniversityResponse;
import first.second.third.repositories.FacultiesAndSubjectsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.validation.Valid;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class FacultiesAndSubjectsService {

    @Autowired
    private FacultiesAndSubjectsRepository facultiesAndSubjectsRepository;

    public List<FacultiesAndSubjectsResponse> getAllFacultiesAndSubjects() {
        return facultiesAndSubjectsRepository.findAll().stream()
                .map(FacultiesAndSubjectsResponse::new)
                .collect(Collectors.toList());
    }

    public List<UniversityResponse> getAllUniversities() {
        return facultiesAndSubjectsRepository.findAll().stream()
                .map(UniversityResponse::new)
                .collect(Collectors.toList());
    }

    public FacultiesAndSubjects addNewFacultiesAndSubjects(@Valid FacultiesAndSubjects facultiesAndSubjects) {
        FacultiesAndSubjects newFacultiesAndSubjects= new FacultiesAndSubjects();


        newFacultiesAndSubjects.setId(facultiesAndSubjects.getId());
        newFacultiesAndSubjects.setFaculty(facultiesAndSubjects.getFaculty());
        newFacultiesAndSubjects.setSubject(facultiesAndSubjects.getSubject());
        newFacultiesAndSubjects.setUniversity(facultiesAndSubjects.getUniversity());


        return facultiesAndSubjectsRepository.save(newFacultiesAndSubjects);
    }

    public void deleteFacultiesAndSubjects(String id) {

        facultiesAndSubjectsRepository.delete(facultiesAndSubjectsRepository.findFacultiesAndSubjectsById(id));

    }

    public void deleteAllFacultiesAndSubjects(){
        facultiesAndSubjectsRepository.deleteAll();
    }



}
