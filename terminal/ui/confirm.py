def confirm_update(self, alias, old_path, new_path):
  confirm = input(f"\nAre you sure you want to update the path for {alias} from {old_path} to {new_path}? (Y/N): ").strip().lower()
  return confirm == 'y'

def confirm_delete(self, alias, old_path):
      confirm = input(f"\nAre you sure you want to delete the path for {alias} -> {old_path}? (Y/N): ").strip().lower()
      return confirm == 'y'