# 3. Commit Message Standards

All commits must follow **Conventional Commits**.

## Format

```
<type>: <imperative description>
```

## Rules

- Use lowercase
- Use imperative mood
- Max 50 characters
- No trailing punctuation
- One logical change per commit

## Allowed Types

| Type       | Description                                          |
| ---------- | ---------------------------------------------------- |
| `feat`     | new feature                                          |
| `fix`      | bug fix                                              |
| `refactor` | code restructuring without behavior change           |
| `perf`     | performance improvements                             |
| `docs`     | documentation updates                                |
| `test`     | test changes                                         |
| `chore`    | non-production code changes                          |
| `ci`       | CI or pipeline changes                               |
| `build`    | build system or dependency changes                   |

## Examples

- `feat: add password reset flow`
- `fix: handle null token edge case`
- `refactor: simplify cache interface`
