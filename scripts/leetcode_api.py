from loguru import logger
import requests

from scripts.lib import Problem


def fetch_problem(slug: str) -> Problem:
    logger.info("Fetching problem data...")

    url = "https://leetcode.com/graphql"

    # Unused: questionFrontendId, likes, dislikes, isPaidOnly
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            title
            content
            isPaidOnly
            difficulty
            topicTags {
                name
            }
        }
    }
    """
    variables = {"titleSlug": slug}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            url, json={"query": query, "variables": variables}, headers=headers
        )
        data = response.json()["data"]["question"]
    except Exception as e:
        logger.error("No connection")
        logger.exception(e)
        exit(1)
    logger.info("... roblem data fetched successfully")
    problem = Problem.from_post(slug, data)
    return problem
