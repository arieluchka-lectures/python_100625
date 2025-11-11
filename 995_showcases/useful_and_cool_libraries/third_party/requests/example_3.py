import requests
from datetime import datetime

def get_user_info(username):
    """
    Fetch public information about a GitHub user.

    Args:
        username (str): GitHub username
    """
    url = f"https://api.github.com/users/{username}"

    print(f"\nFetching information for GitHub user: {username}")
    print("-" * 60)

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print(f"User '{username}' not found.")
            return None

        response.raise_for_status()
        user_data = response.json()

        print(f"\nUser Profile:")
        print(f"  Name: {user_data.get('name', 'N/A')}")
        print(f"  Username: {user_data['login']}")
        print(f"  Bio: {user_data.get('bio', 'N/A')}")
        print(f"  Location: {user_data.get('location', 'N/A')}")
        print(f"  Public Repos: {user_data['public_repos']}")
        print(f"  Followers: {user_data['followers']}")
        print(f"  Following: {user_data['following']}")
        print(f"  Profile URL: {user_data['html_url']}")
        print(f"  Created: {user_data['created_at']}")

        return user_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        return None


def get_user_repositories(username, max_repos=5):
    """
    Fetch public repositories for a GitHub user.

    Args:
        username (str): GitHub username
        max_repos (int): Maximum number of repos to display
    """
    url = f"https://api.github.com/users/{username}/repos"

    # Parameters to sort by most recently updated
    params = {
        'sort': 'updated',
        'direction': 'desc',
        'per_page': max_repos
    }

    print(f"\nFetching top {max_repos} repositories for {username}...")
    print("-" * 60)

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        repos = response.json()

        if not repos:
            print(f"No public repositories found for {username}")
            return []

        print(f"\nTop {len(repos)} Repositories:\n")
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo['name']}")
            print(f"   Description: {repo['description'] or 'No description'}")
            print(f"   Language: {repo['language'] or 'Not specified'}")
            print(f"   Stars: ⭐ {repo['stargazers_count']}")
            print(f"   Forks: 🍴 {repo['forks_count']}")
            print(f"   URL: {repo['html_url']}")
            print(f"   Last Updated: {repo['updated_at']}")
            print()

        return repos

    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return []


def search_repositories(query, max_results=5):
    """
    Search for repositories on GitHub.

    Args:
        query (str): Search query
        max_results (int): Maximum number of results to display
    """
    url = "https://api.github.com/search/repositories"

    params = {
        'q': query,
        'sort': 'stars',
        'order': 'desc',
        'per_page': max_results
    }

    print(f"\nSearching GitHub for: '{query}'")
    print("-" * 60)

    try:
        # GitHub API requires User-Agent header
        headers = {'User-Agent': 'Python-Requests-Tutorial'}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        total_count = data['total_count']
        items = data['items']

        print(f"\nFound {total_count:,} repositories. Showing top {len(items)}:\n")

        for i, repo in enumerate(items, 1):
            print(f"{i}. {repo['full_name']}")
            print(f"   Description: {repo['description'] or 'No description'}")
            print(f"   Language: {repo['language'] or 'Multiple'}")
            print(f"   Stars: ⭐ {repo['stargazers_count']:,}")
            print(f"   Forks: 🍴 {repo['forks_count']:,}")
            print(f"   URL: {repo['html_url']}")
            print()

        return items

    except requests.exceptions.RequestException as e:
        print(f"Error searching repositories: {e}")
        return []


def get_repository_details(owner, repo_name):
    """
    Get detailed information about a specific repository.

    Args:
        owner (str): Repository owner username
        repo_name (str): Repository name
    """
    url = f"https://api.github.com/repos/{owner}/{repo_name}"

    print(f"\nFetching details for {owner}/{repo_name}...")
    print("-" * 60)

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print(f"Repository '{owner}/{repo_name}' not found.")
            return None

        response.raise_for_status()
        repo = response.json()

        print(f"\nRepository Details:")
        print(f"  Name: {repo['full_name']}")
        print(f"  Description: {repo['description'] or 'No description'}")
        print(f"  Language: {repo['language'] or 'Not specified'}")
        print(f"  Stars: ⭐ {repo['stargazers_count']:,}")
        print(f"  Forks: 🍴 {repo['forks_count']:,}")
        print(f"  Open Issues: {repo['open_issues_count']}")
        print(f"  Watchers: {repo['watchers_count']}")
        print(f"  Size: {repo['size']} KB")
        print(f"  Default Branch: {repo['default_branch']}")
        print(f"  Created: {repo['created_at']}")
        print(f"  Last Updated: {repo['updated_at']}")
        print(f"  License: {repo['license']['name'] if repo.get('license') else 'None'}")
        print(f"  URL: {repo['html_url']}")

        return repo

    except requests.exceptions.RequestException as e:
        print(f"Error fetching repository details: {e}")
        return None


def main():
    """Main function to demonstrate GitHub API usage."""
    print("=" * 60)
    print("GITHUB API EXAMPLE - Public Repository Data")
    print("=" * 60)

    # Example 1: Get user information
    get_user_info("torvalds")

    # Example 2: Get user's repositories
    get_user_repositories("gvanrossum", max_repos=3)

    # Example 3: Search for repositories
    search_repositories("machine learning python", max_results=3)

    # Example 4: Get specific repository details
    get_repository_details("psf", "requests")

    # Example 5: Check API rate limits
    print("\n" + "=" * 60)
    print("Checking GitHub API Rate Limits...")
    print("-" * 60)

    try:
        response = requests.get("https://api.github.com/rate_limit")
        rate_data = response.json()

        core = rate_data['resources']['core']
        search = rate_data['resources']['search']

        print(f"\nCore API:")
        print(f"  Limit: {core['limit']} requests/hour")
        print(f"  Remaining: {core['remaining']}")
        print(f"  Resets at: {datetime.fromtimestamp(core['reset'])}")

        print(f"\nSearch API:")
        print(f"  Limit: {search['limit']} requests/minute")
        print(f"  Remaining: {search['remaining']}")

    except requests.exceptions.RequestException as e:
        print(f"Error checking rate limits: {e}")

    print("\n" + "=" * 60)
    print("GitHub API Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
