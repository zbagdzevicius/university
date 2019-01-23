package first.second.third.repositories;

import first.second.third.beans.documents.FacultiesAndSubjects;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface FacultiesAndSubjectsRepository extends CrudRepository<FacultiesAndSubjects, String> {

    List<FacultiesAndSubjects> findAll();

    FacultiesAndSubjects findFacultiesAndSubjectsById(String id);
}
