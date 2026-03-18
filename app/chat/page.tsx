import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { redirect } from "next/navigation";
import { ChatWindow } from "@/components/chat/ChatWindow";

export default async function ChatPage() {
  const session = await getServerSession(authOptions);
  if (!session) redirect("/login");

  // Redirect to onboarding if name not set
  if (!session.user.name) redirect("/onboarding");

  return <ChatWindow />;
}
