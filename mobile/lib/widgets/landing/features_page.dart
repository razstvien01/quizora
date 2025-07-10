import 'package:flutter/material.dart';
import 'package:lucide_icons/lucide_icons.dart';

class FeaturesPage extends StatelessWidget {
  const FeaturesPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const [
          Icon(LucideIcons.brain, size: 48, color: Colors.blue),
          SizedBox(height: 16),
          Text(
            'Personalized Learning',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
          ),
          SizedBox(height: 16),
          Text(
            'Our AI tailors your learning journey, creating custom study plans, mock exams, and progress tracking to help you master your subjects.',
            style: TextStyle(color: Colors.grey, fontSize: 16),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
}
