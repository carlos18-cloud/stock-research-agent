from config.config import TONGYI_API_KEY, TONGYI_BASE_URL, TONGYI_MODEL
from llms.tongyi_llm import TongyiLLM
from agent.research_agent import ResearchAgent
from agent.controller import ResearchController

def main():

    # 1. 初始化 LLM
    llm = TongyiLLM(
        api_key=TONGYI_API_KEY,
        base_url=TONGYI_BASE_URL,
        model=TONGYI_MODEL,
    )

    # 2. 初始化 Agent
    agent = ResearchAgent(llm)

    # 3. 初始化 Controller
    controller = ResearchController(agent)

    # 4. 执行研究
    state = controller.run(
        "研究当前美股市场中最值得关注的 AI 投资机会"
    )

    # 5. 输出结果
    print("\n========== 研究结果 ==========")

    print("\n研究主题：")
    print(state.topic.title if state.topic else state.question)

    print("\n核心投资论点：")
    print(state.thesis.main_thesis)

    print("\n看多逻辑：")
    for item in state.thesis.bull_case:
        print("-", item)

    print("\n看空逻辑：")
    for item in state.thesis.bear_case:
        print("-", item)

    print("\n关键风险：")
    for item in state.thesis.key_risks:
        print("-", item)

    print("\n研究报告：")
    print(state.report.sections[0])

    print("\n========== 运行统计 ==========")
    print("证据数量：", len(state.evidences))
    print("分析次数：", len(state.analyses))
    print("反思次数：", state.reflection_count)


if __name__ == "__main__":
    main()