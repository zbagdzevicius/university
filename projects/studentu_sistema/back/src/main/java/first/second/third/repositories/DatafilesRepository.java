package first.second.third.repositories;

import first.second.third.beans.documents.Datafiles;
import org.bson.types.Binary;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface DatafilesRepository extends CrudRepository<Datafiles, String> {
    List<Datafiles> findAll();
    List<Datafiles> findDatafilesBySubject(String subject);
    List<Datafiles> findDatafilesByUserName(String userName);
    Datafiles findDatafilesByFileName(String fileName);
    void deleteAll();
}
