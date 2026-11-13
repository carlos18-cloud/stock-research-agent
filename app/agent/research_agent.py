from nodes.topic_discovery_node import TopicDiscoveryNode
from nodes.research_planning_node import ResearchPlanningNode
from nodes.search_node import SearchNode
from nodes.news_node import NewsNode
from nodes.evidence_node import EvidenceNode
from nodes.analysis_node import AnalysisNode
from nodes.reflection_node import ReflectionNode
from nodes.judge_node import JudgeNode
from nodes.thesis_node import ThesisNode
from nodes.report_node import ReportNode

from memory.user_profile import UserProfile
from memory.research_history import ResearchHistory

class ResearchAgent:

    def __init__(self, llm):

        self.llm = llm

        # 主题发现与规划
        self.topic_discovery_node = TopicDiscoveryNode(llm)
        self.research_planning_node = ResearchPlanningNode(llm)

        # 信息收集
        self.search_node = SearchNode(llm)
        self.news_node = NewsNode(llm)

        # 证据与分析
        self.evidence_node = EvidenceNode(llm)
        self.analysis_node = AnalysisNode(llm)

        # 反思与判断
        self.reflection_node = ReflectionNode(llm)
        self.judge_node = JudgeNode(llm)

        # 投资论点与报告
        self.thesis_node = ThesisNode(llm)
        self.report_node = ReportNode(llm)

        self.user_profile = UserProfile()
        self.research_history = ResearchHistory()