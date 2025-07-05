import 'package:flutter/material.dart';
import 'package:lucide_icons/lucide_icons.dart';

class KickstartPage extends StatelessWidget {
  const KickstartPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(24),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const [
          Icon(LucideIcons.zap, size: 48, color: Colors.orange),
          SizedBox(height: 16),
          Text(
            'Join Thousands of Learners',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
          ),
          SizedBox(height: 16),
          Text(
            'Kickstart your exam prep journey with Quizora’s AI-powered study platform — built for students like you.',
            style: TextStyle(color: Colors.grey, fontSize: 16),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
}
