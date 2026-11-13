from models.research_state import ResearchState
from models.topic import Topic


class ResearchController:

    def __init__(self, agent):
        self.agent = agent

    def run(self, query: str):

        # 1. 初始化 State
        state = ResearchState(question=query)

        profile = self.agent.user_profile.load()

        # 2. 主题发现
        topics = self.agent.topic_discovery_node.run(
            focus_areas=profile["research_focus"]
        )

        # 4. 选择排名第一的主题
        state.topic = topics[0]

        # 5. 研究规划
        state.research_questions = (
            self.agent.research_planning_node.run(state.topic)
        )

        # 6. 初始信息收集
        self.agent.search_node.run(state)
        self.agent.news_node.run(state)

        # 7. 证据提取与分析
        self.agent.evidence_node.run(state)
        self.agent.analysis_node.run(state)

        # 8. 反思循环
        while state.reflection_count < state.max_reflection_count:

            reflection = self.agent.reflection_node.run(state)

            if not reflection["need_reflection"]:
                break

            state.reflection_count += 1

            new_results = self.agent.search_node.run(
                state,
                query=reflection["reflection_query"],
            )

            self.agent.evidence_node.run(
                state,
                materials=new_results,
            )

            self.agent.analysis_node.run(state)

        # 9. 研究充分性判断
        judgment = self.agent.judge_node.run(state)

        if not judgment["is_sufficient"]:
            print("研究尚不充分：", judgment["reason"])

        # 10. 生成投资论点和报告
        state.thesis = self.agent.thesis_node.run(state)
        state.report = self.agent.report_node.run(state)

        self.agent.research_history.save(state)

        return state