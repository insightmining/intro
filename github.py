import requests

def get_github_user_info_and_repos(username):
    """
    GitHub 사용자 프로필 정보와 저장소 목록을 조회하는 함수.
    
    :param username: GitHub 사용자 이름 (str)
    :return: 사용자의 프로필 정보와 저장소 목록을 포함한 딕셔너리
    """
    base_url = "https://api.github.com/users"
    
    # 사용자 프로필 정보 가져오기
    user_url = f"{base_url}/{username}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        return None  # 오류 발생 시 None 반환

    user_data = user_response.json()  # JSON 데이터를 파싱

    # 사용자 저장소 목록 가져오기
    repos_url = f"{base_url}/{username}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        repos_data = []  # 저장소 정보를 가져오지 못하면 빈 리스트 반환
    else:
        repos_data = repos_response.json()

    return {
        "profile": user_data,
        "repositories": repos_data
    }

# 테스트 실행
if __name__ == "__main__":
    username = "insightmining"  # GitHub에서 존재하는 테스트 계정
    result = get_github_user_info_and_repos(username)

    if result:
        print("사용자 프로필 정보:")
        print(result["profile"])  # 사용자 프로필 정보 출력
        print("\n사용자 저장소 목록:")
        for repo in result["repositories"]:
            print(f"- {repo['name']}: {repo['html_url']}")
    else:
        print("사용자 정보를 가져올 수 없습니다.")

def test_get_github_user_info_and_repos():
    # 정상 상태 테스트: 존재하는 GitHub 사용자
    valid_username = "insightmining"
    user_data = get_github_user_info_and_repos(valid_username)
    
    assert user_data is not None, "사용자 정보가 None이면 안 됩니다."
    assert "profile" in user_data, "프로필 정보가 포함되어야 합니다."
    assert "repositories" in user_data, "저장소 정보가 포함되어야 합니다."
    assert user_data["profile"]["login"] == valid_username, "사용자 로그인 정보가 일치해야 합니다."

    # 비정상 상태 테스트: 존재하지 않는 GitHub 사용자
    invalid_username = "nonexistent_user_123456789"
    user_data = get_github_user_info_and_repos(invalid_username)
    
    assert user_data is None, "존재하지 않는 사용자의 정보는 None이어야 합니다."

    print("모든 테스트 통과!")

# 테스트 실행
test_get_github_user_info_and_repos()


