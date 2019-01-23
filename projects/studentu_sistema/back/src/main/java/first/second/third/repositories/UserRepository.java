package first.second.third.repositories;
import first.second.third.beans.documents.User;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface UserRepository extends CrudRepository<User, String> {
    List<User> findAll();

    User getUserByUserName(String userName);

    String findUserByUserName(String userName);

    String findUserByEmail(String email);

    String findUserByAccessToken(String accessToken);

    void deleteAll();
}